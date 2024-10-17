<!--
Toggle - A Gradio Custom Component
Created by Daniel Ialcin Misser Westergaard
https://huggingface.co/dwancin
https://github.com/dwancin
(c) 2024
-->

<script context="module" lang="ts">
	export { default as BaseCheckbox } from "./shared/Checkbox.svelte";
</script>

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block, Info } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import type { SelectData } from "@gradio/utils";
	import { afterUpdate } from "svelte";

	// Props
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value = false;
	export let color: string = "var(--checkbox-background-color-selected)";
	export let radius: "sm" | "lg" = "lg";
	export let transition: GLfloat = 0.3;
	export let value_is_output = false;
	export let label = "Toggle";
	export let show_label: boolean = true;
	export let info: string | undefined = undefined;
	export let root: string;
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let loading_status: LoadingStatus;
	export let gradio: Gradio<{
		change: never;
		select: SelectData;
		input: never;
		clear_status: LoadingStatus;
	}>;
	export let interactive: boolean;

	// Dispatch change and input events
	function handle_change(): void {
		gradio.dispatch("change");
		if (!value_is_output) {
			gradio.dispatch("input");
		}
	}

	// Toggle the value when the component is activated
	function activateToggle(event: MouseEvent | KeyboardEvent) {
		// Allow toggle only when interactive
		if (interactive) {
			value = !value;
			handle_change();
			event.preventDefault(); // Prevent default behavior (useful for keyboard events)
		}
	}

	// Reset output state after update
	afterUpdate(() => {
		value_is_output = false;
	});
</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
	<StatusTracker
		autoscroll={gradio.autoscroll}
		i18n={gradio.i18n}
		{...loading_status}
		on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
	/>

	{#if info}
		<Info {root} {info} />
	{/if}

	<!-- svelte-ignore a11y-role-supports-aria-props -->
	<!-- svelte-ignore a11y-role-has-required-aria-props -->
	<div
		class="toggle {interactive ? '' : 'non-interactive'}"
		role="switch"
		tabindex="0"
		aria-pressed="{value}"
		aria-label="{show_label ? label : 'Toggle'}"
		on:click={activateToggle}
		on:keydown={(e) => ['Enter', ' '].includes(e.key) && activateToggle(e)}
	>
		<div
			class="toggle-switch"
			class:active={value}
			style="
				background-color: {value ? color : 'var(--border-color-primary)'};
				border-radius: {radius === 'sm' ? 'var(--radius-xs)' : 'var(--radius-xl)'};
				transition: background-color {transition}s, box-shadow {transition}s;
			"
		>
			<div 
				class="toggle-knob"
				style="
					border-radius: {radius === 'sm' ? 'var(--radius-xs)' : 'var(--radius-100)'};
					transition: left {transition}s;
				"
			>
			</div>
		</div>
		{#if show_label}
			<span class="toggle-label">{label}</span>
		{/if}
	</div>
</Block>

<style>
	:root {
		--toggle-width: var(--size-10);
		--toggle-height: var(--size-5);
		--knob-size: var(--spacing-xxl);
		--knob-radius: var(--radius-lg);
		--knob-background-color: white;
		--toggle-gap: var(--spacing-xl);
		--toggle-label-text-color: var(--checkbox-label-text-color);
		--toggle-label-text-size: var(--checkbox-label-text-size);
		--toggle-label-text-weight: var(--checkbox-label-text-weight);
		--toggle-border-color: var(--block-title-border-color);
		--toggle-background-color: var(--border-color-yprimar);
		--toggle-background-color-selected: var(--checkbox-background-color-selected);
		--toggle-shadow: var(--shadow-drop);
	}

	.toggle {
		display: flex;
		align-items: center;
		cursor: pointer;
		user-select: none;
		outline: none;
		gap: var(--toggle-gap);
	}

	.toggle-label {
		display: inline-block;
		position: relative;
		z-index: var(--layer-4);
		border: solid var(--block-title-border-width) var(--toggle-border-color);
		border-radius: var(--block-title-radius);
		background: var(--block-title-background-fill);
		padding: var(--block-title-padding);
		color: var(--toggle-label-text-color);
		font-weight: var(--toggle-label-text-weight);
		font-size: var(--toggle-label-text-size);
	}

	.toggle-switch {
		width: var(--toggle-width);
		height: var(--toggle-height);
		background-color: var(--toggle-background-color);
		position: relative;
		box-shadow: var(--toggle-shadow);
	}

	.toggle-switch.active {
		background-color: var(--toggle-background-color-selected);
	}

	.toggle-knob {
		width: var(--knob-size);
		height: var(--knob-size);
		background-color: white;
		border-radius: var(--radius-lg);
		position: absolute;
		top: 2px;
		left: 2px;
	}

	.toggle-switch.active .toggle-knob {
		left: calc(var(--toggle-width) - var(--knob-size) - 2px);
	}

	.toggle:hover .toggle-switch,
	.toggle:focus .toggle-switch {
		box-shadow: var(--toggle-shadow);
	}

	/* New style for non-interactive state */
	.non-interactive {
		cursor: no-drop;
	}
</style>
