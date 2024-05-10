<script lang="ts">
    // Toggle - A Gradio Custom Component
    // Created by Daniel Ialcin Misser Westergaard
    // https://huggingface.co/dwancin
    // https://github.com/dwancin
    // (c) 2024
    
    import { writable } from 'svelte/store';
    import type { Gradio } from "@gradio/utils";
    import { Block, Info } from "@gradio/atoms";
    import { StatusTracker } from "@gradio/statustracker";
    import type { LoadingStatus } from "@gradio/statustracker";
    import type { SelectData } from "@gradio/utils";
    import { afterUpdate } from "svelte";

    export let value: boolean = false;
    export let label: string = "Toggle";
    export let show_label: boolean = true;
    export let info: string | undefined = undefined;
    export let color: string = "#ea580c";
    export let visible: boolean = true;
    export let container: boolean = true;
    export let scale: number | null = null;
    export let min_width: number | undefined = undefined;
    export let interactive: boolean = true;
    export let elem_classes: string[] = [];
    export let elem_id: string = "";
    
    export let value_is_output = false;
    export let loading_status: LoadingStatus;
    export let gradio: Gradio<{
        change: never;
        select: SelectData;
        input: never;
    }>;

    function handle_keydown(event: KeyboardEvent): void {
        if (event.key === 'Enter' || event.key === ' ') {
            handle_change();
        }
    }

    function handle_change(): void {
        if (interactive) {
            value = !value;
            gradio.dispatch("change");
            if (!value_is_output) {
                gradio.dispatch("input");
            }
        }
    }
    
    afterUpdate(() => {
        value_is_output = false;
    });
</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
    <StatusTracker
        autoscroll={gradio.autoscroll}
        i18n={gradio.i18n}
        {...loading_status}
    />
    
    <div class={elem_classes.join(" ")}>
        {#if show_label}
            <span class="toggle-label" aria-hidden="true">
                {label}
            </span>
        {/if}
        
        <div
            class="toggle {value ? 'active' : ''} {interactive ? '' : 'non-interactive'}"
            on:click={handle_change}
            on:keydown={handle_keydown}
            tabindex="0"
            type="button"
            role="switch"
            aria-checked={value}
            aria-label={label}
            style="background-color: {value ? color : 'var(--border-color-primary)'};"
        ></div>
        
        {#if info}
            <div class="toggle-info">
                <Info>
                    {info}
                </Info>
            </div>
        {/if}
    </div>
</Block>

<style>
    .toggle {
        position: relative;
        margin: -8px 0px;
        width: 58px;
        height: 24px;
        display: inline-block;
        border-radius: 60px;
        background: var(--border-color-primary);
        border-color: transparent;
        border-width: 1px;
        box-shadow: inset 0px 0px 3px 0px #0000001a;
        cursor: pointer;
        transition: var(--button-transition);
    }

    .toggle::after {
        content: '';
        position: absolute;
        margin: 3px 6px;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background-color: white;
        border-color: var(--neutral-50);
        border-width: 1px;
        border-style: solid;
        box-shadow: var(--button-shadow-hover);
        transition: 0.3s;
    }

    .toggle.active::after {
        transform: translateX(28px);
    }

    .toggle.non-interactive {
        cursor: not-allowed;
    }
    
    .toggle-label {
        font-size: var(--checkbox-label-text-size);
        margin-right: var(--spacing-md);
        color: var(--body-text-color);
        cursor: pointer;
        font-weight: var(--checkbox-label-text-weight);
        line-height: var(--line-md);
        font-family: var(--font);
    }
    
    .toggle-info {
        margin-top: var(--spacing-lg);
    }
</style>
