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
    import { writable, get } from 'svelte/store';
    import type { Gradio } from "@gradio/utils";
    import { Block, Info } from "@gradio/atoms";
    import { StatusTracker } from "@gradio/statustracker";
    import type { LoadingStatus } from "@gradio/statustracker";
    import type { SelectData } from "@gradio/utils";
    import { afterUpdate, onMount } from "svelte";

    export let value: boolean = false;
    export let label = "Toggle";
    export let show_label: boolean = true;
    export let visible = true;
    export let info: string | undefined = undefined;
    export let color: string = "var(--checkbox-background-color-selected)";
    export let container = true;
    export let scale: number | null = null;
    export let min_width: number | undefined = undefined;
    export let interactive: boolean = true;
    export let elem_id = "";
    export let elem_classes: string[] = [];
    export let value_is_output = false;
    export let loading_status: LoadingStatus;
    export let gradio: Gradio<{
        change: never;
        select: SelectData;
        input: never;
        clear_status: LoadingStatus;
    }>;

    const valueStore = writable(value);

    function handleChange(): void {
        if (interactive) {
            valueStore.update(v => !v);
            gradio.dispatch("change");
            if (!value_is_output) {
                gradio.dispatch("input");
            }
        }
    }

    function handleKeydown(event: KeyboardEvent): void {
        if (interactive && (event.key === 'Enter' || event.key === ' ')) {
            event.preventDefault();
            handleChange();
        }
    }

    $: valueStore.subscribe(val => {
        value = val;
    });

    afterUpdate(() => {
        value_is_output = false;
    });

    onMount(() => {
        valueStore.set(value);
    });

    $: {
        if (get(valueStore) !== value) {
            valueStore.set(value);
        }
    }
</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
    <StatusTracker
        autoscroll={gradio.autoscroll}
        i18n={gradio.i18n}
        {...loading_status}
        on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
    />
    <div class="block-component">
        <div class="container">
            {#if show_label}
                <div class="block-label" for={elem_id}>{label}</div>
            {/if}
            <div
                id={elem_id}
                on:click={handleChange}
                on:keydown={handleKeydown}
                class="toggle {value ? 'active' : ''} {interactive ? '' : 'non-interactive'}"
                tabindex="{interactive ? '0' : '-1'}"
                role="switch"
                aria-checked={value.toString()}
                aria-label={label}
                style="--toggle-background-color: {value ? color : 'var(--border-color-primary)'};"
            >
                <div class="toggle-knob"></div>
            </div>
        </div>
        {#if info}
            <div id="info" class="block-label-container">
                <div class="block-info">{info}</div>
            </div>
        {/if}
    </div>
</Block>

<style>
    .container {
        display: flex;
        align-items: center;
        justify-content: flex-start;
    }
    .toggle {
        position: relative;
        width: 57px;
        height: 27px;
        display: inline-block;
        border-radius: var(--radius-xxl);
        background: var(--toggle-background-color);
        box-shadow: var(--shadow-inset);
        transition: background-color 0.3s, cursor 0.3s;
        border: solid 0.4px var(--border-color-primary);
        cursor: pointer;
    }
    .toggle.active {
        background: var(--toggle-background-color);
    }
    .toggle-knob {
        position: absolute;
        top: 3px;
        left: 4px;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: white;
        box-shadow: rgba(0, 0, 0, 0.05) 0px 1px 2px 0px;
        transition: transform 0.3s;
    }
    .toggle.active .toggle-knob {
        transform: translateX(27px);
    }
    .toggle.non-interactive {
        cursor: not-allowed;
    }
    .block-label {
        font-size: var(--block-title-text-size);
        margin-right: var(--spacing-md);
        color: var(--block-title-text-color);
        background: var(--block-title-background-fill);
        cursor: default;
        font-weight: var(--block-title-text-weight);
        line-height: var(--line-sm);
        font-family: var(--font);
        display: inline-block;
        position: relative;
    }
    .block-info {
        margin-bottom: var(--spacing-lg);
        color: var(--block-info-text-color);
        font-weight: var(--block-info-text-weight);
        cursor: default;
        font-size: var(--block-info-text-size);
        line-height: var(--line-sm);
    }
</style>
